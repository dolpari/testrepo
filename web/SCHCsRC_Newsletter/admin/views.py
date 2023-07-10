from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.paginator import Paginator
from django.conf import settings
from .gmail.gmail import sendmail
from newsletter.models import trends_Post, reports_Post, trends_PostImage, reports_PostImage, projects_Post, projects_PostImage
from datetime import datetime

import re
import os


# 파일 업로드 제한
def validate_file(request, filename, filetype, filesize):
    valid_value = 0
    file_extension = re.compile(r'.*\.PNG$|.*\.JPEG$|.*\.JPG$|.*\.GIF$', re.I)
    type_check = re.compile(r'image\/.*')
    if(file_extension.match(str(filename)) and type_check.match(str(filetype))):
        if (filesize <= 2):
            valid_value = 1
            return valid_value
        else:
            messages.error(request, '파일 크기가 2MB를 초과합니다.')
            return valid_value
    return valid_value


# 로그인
def login(request):
    if request.method == 'POST':
        admin = request.POST.get('admin')
        password = request.POST.get('password')
        access = authenticate(request, username=admin, password=password)
        if access is not None:
            auth.login(request, access)
            request.session['login_session'] = 'schcsrc'
            return redirect('/admin/index')
        else:
            return render(request, 'admin/login.html', {'error': '아이디 혹은 비밀번호를 다시 확인해주세요.'})
    else:
        return render(request, 'admin/login.html')


# 로그아웃
@login_required(login_url='/admin/')
def logout(request):
    request.session['login_session'] = ''
    auth.logout(request)
    return redirect('/')


# 게시물 수정
@login_required(login_url='/admin/')
def trends_modify(request, post_id):
    modify_post = get_object_or_404(trends_Post, id=post_id)
    modify_images = trends_PostImage.objects.filter(post=modify_post)
    login_session = request.session.get('login_session')
    context = {'modify_post': modify_post,
               'modify_images': modify_images,
               'login_session': login_session}
    # 로그인 여부 확인
    if login_session != 'schcsrc':
        request.session['login_session'] = ''
        messages.error(request, '수정권한이 없습니다.')
        return redirect('/trends/<str:post_id>/')

    # 수정한 내용 가져오기
    if request.method == 'POST':
        modify_post.title = request.POST.get('title')
        modify_post.author = request.POST.get('author')
        modify_post.content = request.POST.get('content')
        modify_post.modified_datetime = timezone.now()
        imageList = request.FILES.getlist('image')

        # 썸네일 변경 확인 : 변경 시 기존 썸네일 삭제
        change_thumbnail = request.FILES.get('thumbnail')
        if change_thumbnail:
            os.remove(os.path.join(settings.MEDIA_ROOT, modify_post.thumbnail.path))
            modify_post.thumbnail = change_thumbnail

        # 체크된 이미지 삭제
        delete_imageList = request.POST.getlist('delete_image', False)
        if delete_imageList:
            for delete_images in delete_imageList:
                correct_image = trends_PostImage.objects.filter(post=modify_post, image=delete_images)
                for deleteImage in correct_image:
                    deleteImage.delete()

        # 게시물 유효성 확인 (필수 요소)
        if modify_post.title and modify_post.author and modify_post.content and modify_post.thumbnail:
            modify_thumbnail_type = modify_post.thumbnail.content_type
            modify_thumbnail_size = modify_post.thumbnail.size
            # 변경할 썸네일 확장자 제한
            if validate_file(request, modify_post.thumbnail, modify_thumbnail_type, modify_thumbnail_size) is None:
                messages.error(request, '올바른 파일을 첨부해 주세요.')
                return render(request, 'admin/modify.html', context)
            modify_post.save()

            # 다중 이미지 파일 확장자 제한 확인 및 저장
            if imageList:
                for image in imageList:
                    image_type = image.content_type
                    image_size = image.size
                    if validate_file(request, image, image_type, image_size) is None:
                        messages.error(request, '올바른 파일을 첨부해 주세요.')
                        return render(request, 'admin/modify.html', context)
                    else:
                        modify_image = trends_PostImage()
                        modify_image.post = modify_post
                        modify_image.image = image
                        modify_image.save()
            return redirect(f'/admin/trends/{modify_post.id}')
        else:
            messages.error(request, '제목, 작성자, 내용, 썸네일은 필수 항목입니다.')
            return render(request, 'admin/modify.html', context)
    else:
        return render(request, 'admin/modify.html', context)
    return redirect(f'/admin/trends/{modify_post.id}/')


# 게시물 수정
@login_required(login_url='/admin/')
def reports_modify(request, post_id):
    modify_post = get_object_or_404(reports_Post, id=post_id)
    modify_images = reports_PostImage.objects.filter(post=modify_post)
    login_session = request.session.get('login_session')
    context = {'modify_post': modify_post,
               'modify_images': modify_images,
               'login_session': login_session}
    # 로그인 확인
    if login_session != 'schcsrc':
        request.session['login_session'] = ''
        messages.error(request, '수정권한이 없습니다.')
        return redirect('/reports/<str:post_id>/', post_id=modify_post.id)

    # 게시물 내용 수정
    if request.method == 'POST':
        modify_post.title = request.POST.get('title')
        modify_post.author = request.POST.get('author')
        modify_post.content = request.POST.get('content')
        modify_post.modified_datetime = timezone.now()
        imageList = request.FILES.getlist('image')

        change_thumbnail = request.FILES.get('thumbnail')
        if change_thumbnail:
            os.remove(os.path.join(settings.MEDIA_ROOT, modify_post.thumbnail.path))
            modify_post.thumbnail = change_thumbnail

        # 체크된 이미지 삭제
        delete_imageList = request.POST.getlist('delete_image', False)
        if delete_imageList:
            for delete_images in delete_imageList:
                correct_image = reports_PostImage.objects.filter(post=modify_post, image=delete_images)
                for deleteImage in correct_image:
                    deleteImage.delete()

        # 게시물 유효성 확인 (필수 요소)
        if modify_post.title and modify_post.author and modify_post.content and modify_post.thumbnail:
            modify_thumbnail_type = modify_post.thumbnail.content_type
            modify_thumbnail_size = modify_post.thumbnail.size / (1024 * 1024)
            # 썸네일 확장자 확인
            if validate_file(request, modify_post.thumbnail, modify_thumbnail_type, modify_thumbnail_size) is None:
                messages.error(request, '올바른 파일을 첨부해 주세요.')
                return render(request, 'admin/modify.html', context)
            modify_post.save()

            # 다중 이미지 확장자 확인 및 저장
            if imageList:
                for image in imageList:
                    image_type = image.content_type
                    image_size = image.size / (1024 * 1024)
                    if validate_file(request, image, image_type, image_size) is None:
                        messages.error(request, '올바른 파일을 첨부해 주세요.')
                        return render(request, 'admin/modify.html', context)
                    else:
                        modify_image = reports_PostImage()
                        modify_image.post = modify_post
                        modify_image.image = image
                        modify_image.save()
            return redirect(f'/admin/reports/{modify_post.id}/')
        else:
            messages.error(request, '제목, 작성자, 내용, 썸네일은 필수 항목입니다.')
            return render(request, 'admin/modify.html', context)
    else:
        return render(request, 'admin/modify.html', context)
    return redirect(f'/admin/reports/{modify_post.id}/')


@login_required(login_url='/admin/')
def projects_modify(request, post_id):
    modify_post = get_object_or_404(projects_Post, id=post_id)
    modify_images = projects_PostImage.objects.filter(post=modify_post)
    login_session = request.session.get('login_session')
    context = {'modify_post': modify_post,
               'modify_images': modify_images,
               'login_session': login_session}
    # 로그인 확인
    if login_session != 'schcsrc':
        request.session['login_session'] = ''
        messages.error(request, '수정권한이 없습니다.')
        return redirect('/projects/<str:post_id>/', post_id=modify_post.id)

    # 게시물 내용 수정
    if request.method == 'POST':
        modify_post.title = request.POST.get('title')
        modify_post.author = request.POST.get('author')
        modify_post.content = request.POST.get('content')
        modify_post.modified_datetime = timezone.now()
        imageList = request.FILES.getlist('image')
        change_thumbnail = request.FILES.get('thumbnail')
        if change_thumbnail:
            os.remove(os.path.join(settings.MEDIA_ROOT, modify_post.thumbnail.path))
            modify_thumbnail_type = modify_post.thumbnail.content_type
            modify_thumbnail_size = modify_post.thumbnail.size / (1024 * 1024)
            if validate_file(request, modify_post.thumbnail, modify_thumbnail_type, modify_thumbnail_size) == 0:
                messages.error(request, '올바른 파일을 첨부해 주세요.')
                return render(request, 'admin/modify.html', context)
            modify_post.thumbnail = change_thumbnail

        # 체크된 이미지 삭제
        delete_imageList = request.POST.getlist('delete_image', False)
        if delete_imageList:
            for delete_images in delete_imageList:
                correct_image = projects_PostImage.objects.filter(post=modify_post, image=delete_images)
                for deleteImage in correct_image:
                    deleteImage.delete()

        # 게시물 유효성 확인 (필수 요소)
        if modify_post.title and modify_post.author and modify_post.content and modify_post.thumbnail:
            modify_post.save()

            # 다중 이미지 확장자 확인 및 저장
            if imageList:
                for image in imageList:
                    image_type = image.content_type
                    image_size = image.size / (1024 * 1024)
                    if validate_file(request, image, image_type, image_size) == 0:
                        messages.error(request, '올바른 파일을 첨부해 주세요.')
                        return render(request, 'admin/modify.html', context)
                    else:
                        modify_image = projects_PostImage()
                        modify_image.post = modify_post
                        modify_image.image = image
                        modify_image.save()
            return redirect(f'/admin/projects/{modify_post.id}/')
        else:
            messages.error(request, '제목, 작성자, 내용, 썸네일은 필수 항목입니다.')
            return render(request, 'admin/modify.html', context)
    else:
        return render(request, 'admin/modify.html', context)
    return redirect(f'/admin/projects/{modify_post.id}/')


@login_required(login_url='/admin/')
def trends_post(request):
    #  To do
    #  1. 로그인 시에만 해당 페이지 접근 가능
    #  2. 이미지 첨부 시 웹 상의 이미지의 위치 고려
    #  3. 작성이 완료되면 작성 완료된 페이지 리다이렉트
    login_session = request.session.get('login_session')
    context = {'login_session': login_session}
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        content = request.POST.get('content')
        imageList = request.FILES.getlist('image')
        thumbnail = request.FILES.get('thumbnail')
        thumbnail_type = thumbnail.content_type
        thumbnail_size = thumbnail.size / (1024 * 1024)
        if title and author and content and thumbnail:
            if validate_file(thumbnail, thumbnail_type, thumbnail_size) == 0:
                messages.error(request, '올바른 파일을 첨부해 주세요.')
                return render(request, 'admin/post.html', context)
            trends_post = trends_Post(title=title, author=author, content=content, thumbnail=thumbnail)
            trends_post.save()
            if imageList:
                for image in imageList:
                    image_type = image.content_type
                    image_size = image.size / (1024 * 1024)
                    if validate_file(image, image_type, image_size) == 0:
                        messages.error(request, '올바른 파일을 첨부해 주세요.')
                        return render(request, 'admin/post.html', context)
            return redirect(f'/admin/trends/{trends_post.id}')
        else:
            messages.error(request, '제목, 작성자, 내용, 썸네일은 필수 항목입니다.')
            return render(request, 'admin/post.html', context)
    else:
        return render(request, 'admin/post.html', context)


@login_required(login_url='/admin/')
def reports_post(request):
    login_session = request.session.get('login_session')
    context = {'login_session': login_session}
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        content = request.POST.get('content')
        imageList = request.FILES.getlist('image')
        thumbnail = request.FILES.get('thumbnail')
        thumbnail_type = thumbnail.content_type
        thumbnail_size = thumbnail.size / (1024 * 1024)
        if title and author and content and thumbnail:
            if validate_file(request, thumbnail, thumbnail_type, thumbnail_size) == 0:
                messages.error(request, '올바른 파일을 첨부해 주세요.')
                return render(request, 'admin/post.html', context)
            reports_post = reports_Post(title=title, author=author, content=content, thumbnail=thumbnail)
            reports_post.save()

            if imageList:
                for image in imageList:
                    image_type = image.content_type
                    image_size = image.size / (1024 * 1024)
                    if validate_file(request, image, image_type, image_size) == 0:
                        messages.error(request, '올바른 파일을 첨부해 주세요.')
                        return render(request, 'admin/post.html', context)
            return redirect(f'/admin/reports/{reports_post.id}')
        else:
            messages.error(request, '제목, 작성자, 내용, 썸네일은 필수 항목입니다.')
            return render(request, 'admin/post.html', context)
    else:
        return render(request, 'admin/post.html', context)


@login_required(login_url='/admin/')
def projects_post(request):
    login_session = request.session.get('login_session')
    context = {'login_session': login_session}
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        content = request.POST.get('content')
        imageList = request.FILES.getlist('image')
        thumbnail = request.FILES.get('thumbnail')
        thumbnail_type = thumbnail.content_type
        thumbnail_size = thumbnail.size / (1024 * 1024)
        if title and author and content and thumbnail:
            if validate_file(request, thumbnail, thumbnail_type, thumbnail_size) == 0:
                messages.error(request, '올바른 파일을 첨부해 주세요.')
                return render(request, 'admin/post.html', context)
            projects_post = projects_Post(title=title, author=author, content=content, thumbnail=thumbnail)
            projects_post.save()

            if imageList:
                for image in imageList:
                    image_type = image.content_type
                    image_size = image.size / (1024 * 1024)
                    if validate_file(request, image, image_type, image_size) == 0:
                        messages.error(request, '올바른 파일을 첨부해 주세요.')
                        return render(request, 'admin/post.html', context)
                    projects_image = projects_PostImage(post=projects_post, image=image)
                    projects_image.save()
            return redirect(f'/admin/projects/{projects_post.id}')
        else:
            messages.error(request, '제목, 작성자, 내용, 썸네일은 필수 항목입니다.')
            return render(request, 'admin/post.html', context)
    else:
        return render(request, 'admin/post.html', context)


@login_required(login_url='/admin/')
def trends_delete(request, post_id):
    login_session = request.session.get('login_session')
    post = get_object_or_404(trends_Post, id=post_id)
    post_image = trends_PostImage.objects.filter(post=post)
    if login_session == 'schcsrc':
        if post_image:
            for image in post_image:
                image.delete()
        post.delete()
        return redirect('/admin/trends/trends_list/')
    else:
        return redirect(f'/admin/trends/{post_id}/')


@login_required(login_url='/admin/')
def reports_delete(request, post_id):
    login_session = request.session.get('login_session')
    post = get_object_or_404(reports_Post, id=post_id)
    post_image = reports_PostImage.objects.filter(post=post)
    if login_session == 'schcsrc':
        if post_image:
            for image in post_image:
                image.delete()
        post.delete()
        return redirect('/admin/reports/reports_list/')
    else:
        return redirect(f'/admin/reports/{post_id}/')


@login_required(login_url='/admin/')
def projects_delete(request, post_id):
    login_session = request.session.get('login_session')
    post = get_object_or_404(projects_Post, id=post_id)
    post_image = projects_PostImage.objects.filter(post=post)
    if login_session == 'schcsrc':
        if post_image:
            for image in post_image:
                image.delete()
        post.delete()
        return redirect('/admin/projects/projects_list/')
    else:
        return redirect(f'/admin/projects/{post_id}/')
